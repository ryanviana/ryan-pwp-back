import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type BlogPostDocument = HydratedDocument<BlogPost>;

@Schema()
export class RelatedPost {
  @Prop() slug: string;
  @Prop() title: string;
  @Prop() coverImage: string;
}

@Schema({ timestamps: true })
export class BlogPost {
  @Prop({ unique: true, required: true })
  slug: string;

  @Prop({ required: true })
  title: string;

  @Prop({ required: true })
  date: string;

  @Prop({ required: true })
  excerpt: string;

  @Prop({ required: true })
  coverImage: string;

  @Prop({ required: true })
  readingTime: string;

  @Prop({ type: [String], default: [] })
  tags: string[];

  @Prop({ required: true })
  content: string;

  @Prop({ type: [Object], default: [] })
  relatedPosts: RelatedPost[];
}

export const BlogPostSchema = SchemaFactory.createForClass(BlogPost);
