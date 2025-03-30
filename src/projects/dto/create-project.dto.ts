import {
  IsString,
  IsArray,
  IsOptional,
  IsNotEmpty,
  IsBoolean,
  IsUrl,
} from 'class-validator';

export class CreateProjectDto {
  @IsString()
  @IsNotEmpty()
  title: string;

  @IsString()
  @IsNotEmpty()
  description: string;

  @IsString()
  @IsOptional()
  fullDescription?: string;

  @IsString()
  @IsNotEmpty()
  image: string;

  @IsArray()
  @IsString({ each: true })
  @IsOptional()
  tags: string[];

  @IsString()
  @IsNotEmpty()
  slug: string;

  @IsString()
  @IsUrl()
  @IsOptional()
  demoUrl?: string;

  @IsString()
  @IsUrl()
  @IsOptional()
  githubUrl?: string;

  @IsArray()
  @IsString({ each: true })
  @IsOptional()
  features?: string[];

  @IsBoolean()
  @IsOptional()
  featured?: boolean;
}
