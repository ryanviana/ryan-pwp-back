import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { SkillCategoryService } from './skill-category.service';
import { SkillCategoryController } from './skill-category.controller';
import {
  SkillCategory,
  SkillCategorySchema,
} from './entities/skill-category.entity';

@Module({
  imports: [
    MongooseModule.forFeature([
      { name: SkillCategory.name, schema: SkillCategorySchema },
    ]),
  ],
  controllers: [SkillCategoryController],
  providers: [SkillCategoryService],
})
export class SkillCategoryModule {}
